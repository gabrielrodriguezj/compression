# Compression algorithms
This purpose of this repo is to store the implementation of the most populars algorithms.

## Huffman
In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression. The process of finding or using such a code proceeds by means of Huffman coding, an algorithm developed by David A. Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes".

The output from Huffman's algorithm can be viewed as a variable-length code table for encoding a source symbol (such as a character in a file). The algorithm derives this table from the estimated probability or frequency of occurrence (weight) for each possible value of the source symbol. As in other entropy encoding methods, more common symbols are generally represented using fewer bits than less common symbols. Huffman's method can be efficiently implemented, finding a code in time linear to the number of input weights if these weights are sorted. However, although optimal among methods encoding symbols separately, Huffman coding is not always optimal among all compression methods - it is replaced with arithmetic coding or asymmetric numeral systems if better compression ratio is required.

#### Links
* https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
* https://www.programiz.com/dsa/huffman-coding
* https://www.tutorialspoint.com/Huffman-Coding-Algorithm
* https://brilliant.org/wiki/huffman-encoding/

<br/>
<br/>
<br/>

## LZW
Lempel–Ziv–Welch (LZW) is a universal lossless data compression algorithm created by Abraham Lempel, Jacob Ziv, and Terry Welch. It was published by Welch in 1984 as an improved implementation of the LZ78 algorithm published by Lempel and Ziv in 1978. The algorithm is simple to implement and has the potential for very high throughput in hardware implementations. It is the algorithm of the widely used Unix file compression utility compress and is used in the GIF image format. 

#### Links
* https://www.dspguide.com/ch27/5.htm
* https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/
* http://www.cs.columbia.edu/~allen/S14/NOTES/lzw.pdf
* https://users.cs.cf.ac.uk/Dave.Marshall/Multimedia/node214.html
* https://www.youtube.com/watch?v=8Hxo1bPPgCU (spanish)
* https://www.youtube.com/watch?v=fiAReFNIrKc (spanish)


<br/>
<br/>
<br/>

## Improvements
* Calculate the compression ratio
* Process audio,images and files
* better design of the classes
* Add algorithms
