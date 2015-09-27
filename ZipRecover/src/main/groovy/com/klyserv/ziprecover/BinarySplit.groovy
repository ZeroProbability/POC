package com.klyserv.ziprecover
/**
 * Split a binary file based on signature
 *
 * Created by anbu on 27/09/15.
 */
class BinarySplit {

    byte[] signature
    InputStream inStream

    void split(BinaryFileWriter fileWriter) {
        assert signature.size() > 0

        def inputStream =new BufferedInputStream(inStream, 4*1024*1024)
        OutputStream outStream =new BufferedOutputStream(fileWriter.startWriting());

        int readByte
        boolean contentExists=false
        while((readByte=inputStream.read())!=-1) {
            if(readByte==signature[0]) {
                inputStream.mark(signature.size()+1) // mark the position so that we can return to it

                byte[] nextNBytes=new byte[signature.size()]
                inputStream.read(nextNBytes, 1, signature.size()-1)
                nextNBytes[0]=readByte
                if(Arrays.equals(signature, nextNBytes)) {
                    if(contentExists) {
                        contentExists=false
                        outStream.close()
                        fileWriter.endWriting()
                        outStream = new BufferedOutputStream(fileWriter.startWriting())
                    }
                    outStream.write(signature[0])
                } else {
                    contentExists=true
                    outStream.write(readByte)
                }

                inputStream.reset() // return to old position
            } else {
                contentExists=true
                outStream.write(readByte)
            }

        }
        outStream.close()
        fileWriter.endWriting()

    }

    static void main(String[] args) {
        File zipFile=new File('/home/anbu/Downloads/test.zip')
        def bfwi=new BinaryFileWriterImpl(inputFile: zipFile)

        new BinarySplit(inStream: new FileInputStream(zipFile), signature: [0x50, 0x4B, 0x03, 0x04] as byte[]).split(bfwi)
    }

}
