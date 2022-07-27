#!/bin/bash -eu

cd -- "${0%/*}"
script_dir="$(pwd)"
A=$(echo {A..Z})
for i in $A
do
    file="${script_dir}/${i}.py"
    cp "${script_dir}/test.py" "${file}"
done
