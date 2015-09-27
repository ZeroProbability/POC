package com.klyserv.ziprecover

/**
 * Created by anbu on 27/09/15.
 */
class StringBinaryFileWriter implements BinaryFileWriter {
    @Override
    OutputStream startWriting() {
        accumulator=new ByteArrayOutputStream(1024*1024*4)
        return accumulator
    }

    List<byte[]> accumulatorList=new ArrayList<>()
    ByteArrayOutputStream accumulator

    @Override
    void endWriting() {
        accumulatorList.add(accumulator.toByteArray())
    }
}
