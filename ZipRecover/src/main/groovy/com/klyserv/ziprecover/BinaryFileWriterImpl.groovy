package com.klyserv.ziprecover

/**
 * Created by anbu on 27/09/15.
 */
class BinaryFileWriterImpl implements BinaryFileWriter {

    File inputFile
    int counter=1
    FileOutputStream fos

    @Override
    OutputStream startWriting() {
        File outputFile=new File("${inputFile.canonicalPath}_${String.format('%04d', counter++)}")
        fos=new FileOutputStream(outputFile)
    }

    @Override
    void endWriting() {
        fos.close()
    }
}
