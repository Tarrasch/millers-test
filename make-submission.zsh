#!/bin/zsh

#
#     A report named (yourfirstname)(yourlastname)_Project_1 describing the rationale, architecture, and algorithms of your program in accordance #3 above. This document can be a .pdf, .doc, or .docx file.
#     A folder named Source Code that contains the entire source code of your project. Make sure to include any libraries or files that would be necessary to recompile the project.
#     A folder named Representations that has the Propositional Representations of your problems in .txt format. Each representation should be the project number followed by the problem number; for example, Problem 2 of Project 1 should be named 1-2.txt.
#     An executable file named (yourfirstname)(yourlastname)_Project_1 in the root folder of the .zip file that, when run, will solve the problems in the Representations folder.
#         If your project is written in Java, this should be (yourfirstname)(yourlastname)_Project_1.jar.
#         If your project is written in C#, this should be (yourfirstname)(yourlastname)_Project_1.exe.
#         If your project is written in Python, this should be (yourfirstname)(yourlastname)_Project_1.py.
#     It is fine to include other folders in the .zip file if necessary (for example, a lib folder that the .jar file accesses) so long as the above two folders and two files are present.

. ~/.zshrc

# init vars
id=1
pid="Project_$id"
name="ArashRouhani"
npid="${name}_${pid}"
s="submission"

# fresh dir, no zip
rm -rf $s
mkdir $s
rm submission.zip

# create and copy stuff over
pandoc README.markdown -o "$s/$npid.pdf"
cp -r src $s/src
cp main.py $s/$npid.py
mkdir $s/reps
mapl "cp \$1 $s/reps/${id}-\${1/yaml/txt}" ?.yaml
cp "big.yaml" "$s/reps/performence.txt"
cp "subtraction-test.yaml" "$s/reps/subtraction-test.txt"
cp -r yaml $s
eachl "rm $s/src/.*.\$1" swp swo
rm $s/src/*.pyc

zip -r submission $s/*

