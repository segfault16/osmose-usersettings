import re
with open ('state.txt', 'r' ) as f:
    content = f.read()
    # number of lines divided by 16
    num_lines = len(content.splitlines())
    num_files = num_lines // 16
    # split content into num_files
    for i in range(num_files):
        with open ('state_{}.txt'.format(i), 'w' ) as f:
            # write 16 lines to file
            for j in range(16):
                f.write('{}'.format(j) + ',' + content.splitlines()[i*16+j] + '\n')
            # close file
            f.close()



            