from __future__ import with_statement
import sys,os
from fabric.api import run, env, hide, get, parallel, cd
from fabric.operations import put

env.use_ssh_config = True
env.hosts = ["7kr","apink","djb"]



@parallel
def testblake2b(distfile):
    basename = os.path.basename(distfile)
    workdir = basename.replace(".tar.gz","")
    with hide("output","running","stdout","status","warnings"):
        run("rm -rf blake2test")
        run("mkdir -p blake2test")
        put(distfile,"blake2test/" + basename)
        with cd("blake2test"):
            run("tar -xzf " + basename)
            with cd(workdir):
                run("python setup.py build")
                with cd("build"):
                    lib_directory = run("ls | grep lib.")
                    with cd(lib_directory.strip()):
                        # execute python and get result
                        blake2b_result = run("""python -c 'import blake2;print blake2.blake2("blake2",key="blake2");' """)
                        blake2s_result = run("""python -c 'import blake2;print blake2.blake2s("blake2",key="blake2");' """)
                        print env.host , lib_directory.strip() ,  blake2b_result
                        print env.host , lib_directory.strip() ,  blake2s_result
