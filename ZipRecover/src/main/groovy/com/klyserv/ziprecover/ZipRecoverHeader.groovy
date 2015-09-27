package com.klyserv.ziprecover

/**
 * Created by anbu on 26/09/15.
 */
class ZipRecoverHeader {
    public static Short readShort(RandomAccessFile file) {
        int ch1=file.read()
        int ch2=file.read()
        if ((ch1 | ch2) < 0)
            throw new EOFException();
        return (short)((ch2 << 8) + (ch1 << 0));
    }

    public static int readInt(RandomAccessFile file) {
        int ch1=file.read()
        int ch2=file.read()
        int ch3=file.read()
        int ch4=file.read()
        if ((ch1 | ch2 | ch3 | ch4) < 0)
            throw new EOFException();
        return (int)((ch4 << 24) +(ch3 << 16) + (ch2 << 8) + (ch1 << 0));
    }

    public static void main(String[] args) {
        String fname = 'Pics-broken'
        File inFile = new File("/home/anbu/Downloads/${fname}.zip")

        RandomAccessFile rfile = new RandomAccessFile(inFile, "r")

        rfile.seek(0)

        int m
        for (int i=0;i< 10; i++) {
            assert (char) rfile.readByte() == 'P'
            assert (char) rfile.readByte() == 'K'
            m=(int) (rfile.readByte());assert m == 3
            assert rfile.readByte() == 4                      // 4

            def version = readShort(rfile)
            println "version: $version"                      // 4 + 2
            def bitField = readShort(rfile)
            println "bitField: $bitField"                   // 6 + 2
            def compressionMethod = readShort(rfile)
            println "compressionMethod: $compressionMethod"    // 8 + 2
            def dtTime = readInt(rfile)
            println dtTime                        // 10 + 4
            def fileCrc = readInt(rfile)
            println fileCrc                      // 14 + 4
            def compressSize = readInt(rfile)
            println "compressed size: $compressSize"     // 18 + 4
            def uncompressSize = readInt(rfile)
            println "uncompressed size: $uncompressSize"     // 22 + 4
            def fileNameLen = readShort(rfile)
            println "fileName len: $fileNameLen"    // 26 + 2
            def xtraFieldLen = readShort(rfile)
            println "extra field len: $xtraFieldLen"    // 28 + 2
            byte[] aryFileName = new byte[fileNameLen]
            rfile.read(aryFileName)
            byte[] xtraField = new byte[xtraFieldLen]
            rfile.read(xtraField)

            rfile.skipBytes(compressSize)
            def currentLoc=rfile.getFilePointer()
            rfile.seek(currentLoc-10)
            byte[] tailStr = new byte[20]
            rfile.read(tailStr)
            rfile.seek(currentLoc)
            println "Tail string: ${new String(tailStr)}"

            println "file >>>>>> ${new String(aryFileName)}"
        }

    }

}
