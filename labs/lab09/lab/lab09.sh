#!/bin/bash
HELL=HELLO
function hello {
    LOCAL HELLO=World
    echo $HELLO
}
echo $HELLO
hello
