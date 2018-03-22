import os
import sys
import re
import subprocess

def main():

    files = os.listdir(sys.argv[1])

    pattern = '_(\d*)(\.png|\.jpg)$'

    def comparator(list_item):
        m = re.search(pattern, list_item)
        return int(m.group(1))

    image_files = list(filter( lambda x: x.endswith(".png") or
                              x.endswith(".jpg") , files))
    image_files = list(filter( lambda x: re.search(pattern, x), image_files))

    image_files.sort(key=comparator)

    for img in image_files:
        print(img)

    reference = os.path.join(sys.argv[1], image_files[-1])

    outputfilename = os.path.join(sys.argv[1], "results.txt")

    with open(outputfilename, "a") as results:

        for file in image_files[:-1]:
            output_name = os.path.join(sys.argv[1], str(comparator(file))
                                                        + ".png")
            command = "compare -metric PSNR {0} {1} {2}".format(reference,
                                                                os.path.join(sys.argv[1], file),
                                                                output_name)
            print(command)
            output = subprocess.run(command.split(), stderr=subprocess.PIPE)
            results.write("{} {}\n".format(os.path.basename(os.path.splitext(output_name)[0]),
                                                    output.stderr.decode('utf-8')))

main()
