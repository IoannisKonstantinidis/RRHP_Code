#!/usr/bin/env python
import re

with open('list_of_sam_files', 'r') as inp:
        for line in inp:
                L = line.split()
		filename = L[8]
		outfile = filename.replace('.sam', '_output.tsv')
		f_out = open(outfile, 'w')
		pattern = re.compile(r'\s+')
		with open(filename, 'r') as f:
		    for line in f:
		        if line.startswith('@PG'):
		            break
		    for line in f:
		        fields = pattern.split(line)
		        try:
		            strand = int(fields[1])
		        except Exception:
		            continue
		        if strand in (0, 16):
		            ID = fields[2]
		            position = int(fields[3])
		            seq = fields[9]
		            towrite = True
		            if seq.startswith('CCGG'):
		                position += 1
		            elif seq.endswith('CCGG'):
		                position += len(seq)
		                position -= 2
		            else:
		                towrite = False
		            if towrite:
		                f_out.write('{}\t{}\t{}\n'.format(ID, position, strand))
		f_out.close()


