# Build stage
FROM python:alpine3.7

RUN pip3 install nbconvert click ipython
COPY converter.py /
ENTRYPOINT "python3" "/converter.py" "--src_file" "$JUPYTER_FILE" "--output_file" "$OUTPUT_FILE" "--build_dir" "$BUILD_DIR"
