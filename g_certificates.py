#!/usr/bin/python
# coding: utf-8
import os
import sys
import re
import csv


# Generate pdf file
def generate_pdf(filename, directory):
    print "    generating pdf certificate"
    command = 'inkscape %s.svg --export-pdf=%s/%s.pdf' % (filename, directory, filename)
    os.system(command)
    print "    removing svg file"
    remover = 'rm %s.svg' % (filename)
    os.system(remover)

# Generate svg file
def generate_svg(svg_name, svg_file, filename, name):
    print "    copying the svg file from " + filename + ".svg"
    command = 'cp %s.svg %s.svg' % (svg_name, filename)
    os.system(command)
    
    new_certificate = open(filename + ".svg",'r+')
    new_certificate.write( re.sub("___NAME___", name, svg_file) )
    new_certificate.close()

# Generate the certificates
def generate_certificates(svg_name, svg_file, list_names_file, directory):
    list_names = open(list_names_file)
    
    if not os.path.exists(directory):
	os.makedirs(directory)
    
    for name in list_names:
        name = name.rstrip("\n")
        
	if (name):
	    print "Generating " + name + "'s certificate:\n"
            filename = name.replace(" ","_")

	    generate_svg(svg_name, svg_file, filename, name)
            generate_pdf(filename, directory)

if __name__ == '__main__':
    if(len(sys.argv) != 4):
        print "Usage: python g_certificates.py <svg_file> <list_of_names> <folder>"
        sys.exit()
    
    svg_name = sys.argv[1]  # SVG file
    list_names_file = sys.argv[2]  # List of names for generate the certificates
    directory = sys.argv[3]  # Directory for storage the certificates

    svg_file = open(svg_name+".svg").read()  # Open and read the SVG file

    generate_certificates(svg_name, svg_file, list_names_file, directory)
