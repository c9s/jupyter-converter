import nbconvert as nb
import io
import json
import click
import sys

OUTPUT_FORMAT = "script"

"""
The ipython command will start with % and we will skip all of them
"""
def remove_ipython_cells(data):
    result = []
    for c in data:
        if c["cell_type"] == "code":
            if len(c["source"]) > 0:
                command = c["source"][0]
                if command[0] == "%":
                    continue
        result.append(c)
    return result

def init_nbconvert(output_dir):
    cls = nb.exporters.base.get_exporter(OUTPUT_FORMAT)
    exporter = cls()

    writer = nb.writers.files.FilesWriter()
    writer.build_directory = output_dir
    return exporter, writer


@click.command()
@click.option('--src_file', type=str, help = 'source file of notebook_name')
@click.option('--output_file', type=str, help = 'output file name')
@click.option('--build_dir', type=str, help = 'the directory of build workspace')
def main(src_file, output_file, build_dir):
    if src_file is None or output_file is None or build_dir is None:
        print("You should specify the input/output file name and build dir")
        exit(0)

    print("The build directory is {}".format(build_dir))
    print("Ready to convert {} to {}.py".format(src_file, output_file))

    print("Loading the ipython file")
    try:
        data = json.load(open(src_file))
        data["cells"] = remove_ipython_cells(data["cells"])
        input_buffer = io.StringIO(str(json.dumps(data)))
    except:
        print("Handle JSON fails : Unexpected error:", sys.exc_info()[0])
        exit(0)

    print("Init the converter")
    try:
        exporter,writer = init_nbconvert(build_dir)
    except:
        print("Init nbconvert fails :Unexpected error:", sys.exc_info()[0])
        exit(0)

    print("Converting the ipython to python")
    try:
        output, resources = exporter.from_file(input_buffer)
        writer.write(output, resources, notebook_name=output_file)
    except:
        print("Output fails: Unexpected error:", sys.exc_info()[0])
        exit(0)

if __name__ == '__main__':
    main()
