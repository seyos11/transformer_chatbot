#!/bin/bash

IMAGE_NAME='transformer_chatbot'

sudo docker run -it --rm -v $(pwd)/parameters:/workspace/parameters   \
                                -v $(pwd)/checkpoints:/workspace/checkpoints \
                                --network host --entrypoint "python" $IMAGE_NAME "wild.py" "$@" "-rbu" "http://0.0.0.0:9200" "-bi" ""
