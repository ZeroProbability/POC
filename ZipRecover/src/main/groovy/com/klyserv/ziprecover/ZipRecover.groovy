package com.klyserv.ziprecover

/**
 * Created by anbu on 26/09/15.
 */
class ZipRecover {
    public static void breakFile(File infile, File outfile) {
        // read binary file and covert all cr to cr-lf like ascii ftp transfer would do

        byte[] buffer = new byte[1000]
        byte[] writeBuffer=new byte[2000]
        def br=new BufferedInputStream(new FileInputStream(infile))
        def or=new BufferedOutputStream(new FileOutputStream(outfile))

        int nread
        while((nread=br.read(buffer))!=-1) {
            int nwrite=0
            for(int i=0;i<nread; i++) {
                def chr=buffer[i]
                if(chr==10) {
                    writeBuffer[nwrite++]=13
                    writeBuffer[nwrite++]=10
                } else {
                    writeBuffer[nwrite++]=chr
                }
            }
            or.write(writeBuffer, 0, nwrite)
        }
        or.close()
        br.close()
    }

    public static void tryUnbreak(File infile, File outfile) {
        // read binary and convert all cr-lf to lf

        byte[] buffer = new byte[1000]
        byte[] writeBuffer=new byte[2000]
        def br=new BufferedInputStream(new FileInputStream(infile))
        def or=new BufferedOutputStream(new FileOutputStream(outfile))

        int nread
        int bufStart=0
        int lenToRead=buffer.size()
        int fixCount=0
        while((nread=br.read(buffer, bufStart, lenToRead))!=-1) {
            int nwrite=0
            int i
            for(i=0;i<(bufStart+nread-1); i++) {
                def chr=buffer[i]
                def chrnext=buffer[i+1]
                if(chr==13 && chrnext==10) {
                    fixCount++
                    writeBuffer[nwrite++]=10
                    i++
                } else {
                    writeBuffer[nwrite++]=chr
                }
            }
            if(i<buffer.size()-1) {
                // End of file
                writeBuffer[nwrite++]=buffer[i]
            } else if(i==buffer.size()-1) {
                buffer[0] = buffer[i]
                bufStart = 1
                lenToRead = buffer.size() - 1
            } else {
                bufStart = 0
                lenToRead = buffer.size()
            }
            or.write(writeBuffer, 0, nwrite)
        }
        or.close()
        br.close()
        println "Fixed ${fixCount} instances"
    }

    public static void main(String[] args) {
        String fname='test'
        File inFile =new File("/home/anbu/Downloads/${fname}.zip")
        File outFile =new File("/home/anbu/Downloads/${fname}-broken.zip")
        File outFile2=new File("/home/anbu/Downloads/${fname}-unbroken.zip")

        breakFile(inFile, outFile)
        tryUnbreak(outFile, outFile2)
    }
}
