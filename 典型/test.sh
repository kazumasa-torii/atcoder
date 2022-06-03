#!/bin/bash -eu

cd -- "${0%/*}"
script_dir="$(pwd)"
for ((i=1; i<91; i++))
do
    file="${script_dir}/${i}.py"
    cp "${script_dir}/test.py" "${file}"
done
