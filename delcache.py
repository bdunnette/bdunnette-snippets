import os.path, time, sys

wait_secs = 300
userlist = []

try:
    for i in range(1, len(sys.argv)):
        userlist.append(sys.argv[i])
    while len(userlist) > 0:
        for username in userlist:

            notesroot = os.path.join("Z:\\" + username + "\\Notes\\data\\")
            noteslock = os.path.join(notesroot, "~notes.lck")
            perweb = os.path.join(notesroot, "perweb.nsf")
            cache = os.path.join(notesroot, "Cache.NDK")
            filelist = (cache, perweb)

            if os.path.exists(noteslock):
                print time.strftime("%I:%M:%S %p", time.localtime()) + ": Directory " + notesroot + " is locked, skipping..."

            else:
                for filepath in filelist:
                    if os.path.exists(filepath):
                        print time.strftime("%I:%M:%S %p", time.localtime()) + ": Deleting " + filepath
                        os.remove(filepath)
                    else:
                        print time.strftime("%I:%M:%S %p", time.localtime()) + ": " + filepath + " not found, skipping..."

                userlist.remove(username)
                
        if len(userlist) > 0:
            print time.strftime("%I:%M:%S %p", time.localtime()) + ": Waiting " + str(wait_secs) + " seconds..."
            time.sleep(wait_secs)
        
except:
    print "Unexpected error: ", sys.exc_info()[0]
    raise

