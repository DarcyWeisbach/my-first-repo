import numpy as np
import subprocess
import sys,os
AmpData = []
mbed_flg = False
if __name__ == "__main__":
    with open("Parameters.txt", "r") as paramf:#get params
        paramlist = paramf.readlines()
        for param in paramlist:
            if "name" in param: #format exeption
                phrase = param.split()[2]#ブロックありかブロックなしを読み取り
                continue
            exec(param) # execute "param = val"
        fn = int(round(np.math.sqrt(k/M)*30/np.math.pi, 0))
        print("固有振動数[rpm]:", fn)
    #main process
    for freq in range(0,2200,50):
        if os.path.exists(phrase+str(freq)+".csv"):
            os.remove(phrase+str(freq)+".csv")
        if freq > fn-100 and not(mbed_flg):#before, mbed high resolution data
            #hi-res begin ****************************************************************************************
            for freq_ in range(int(fn-100), int(fn+100)):
                if os.path.exists(phrase+str(freq_)+".csv"):
                    os.remove(phrase+str(freq_)+".csv")
                if not(freq_ % 10 == 0  or  fn-4 < freq_ < fn+4):
                    continue
                with subprocess.Popen("強制振動.bat", stdin=subprocess.PIPE) as fv:
                    fv.communicate(str(freq_).encode("utf-8"))
                    fv.wait()
                
                with open(phrase+str(freq_)+".csv", "r") as tf:#read raw file
                    csvstr = tf.read()
                    moddata = csvstr.splitlines()[15:]

                    with open("__temp__.csv", "w") as tempf:#put regular file(temporary)
                        for line_ in moddata:
                            tempf.writelines(line_+"\n")
                
                data = np.loadtxt("__temp__.csv", delimiter=",").T
                AmpData.append([freq_, np.max(data[2])])
                os.remove(phrase+str(freq_)+".csv")


            mbed_flg = True
            continue

            #hi-res end *******************************************************************************************


        with subprocess.Popen("強制振動.bat", stdin=subprocess.PIPE) as fv:
            fv.communicate(str(freq).encode("utf-8"))
            fv.wait()
        
        with open(phrase+str(freq)+".csv", "r") as tf:#read raw file
            csvstr = tf.read()
            moddata = csvstr.splitlines()[15:]

            with open("__temp__.csv", "w") as tempf:#put regular file(temporary)
                for line_ in moddata:
                    tempf.writelines(line_+"\n")
        
        data = np.loadtxt("__temp__.csv", delimiter=",").T
        AmpData.append([freq, np.max(data[2])])
        os.remove(phrase+str(freq)+".csv")

            

    #end process
    os.remove("__temp__.csv")
    print(AmpData)
    np.savetxt('./'+phrase+".csv", AmpData, fmt="%.16f", delimiter=",")
