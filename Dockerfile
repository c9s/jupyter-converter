# Build stage
FROM python:alpine3.6

RUN pip3 install nbconvert click ipython
COPY python/jupyter-converter/converter.py /
ENTRYPOINT "python3" "/converter.py" "--src_file" "$JUPYTER_FILE" "--output_file" "$OUTPUT_FILE" "--build_dir" "$BUILD_DIR"
