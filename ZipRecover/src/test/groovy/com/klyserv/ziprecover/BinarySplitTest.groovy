package com.klyserv.ziprecover

import spock.lang.Specification

/**
 * Created by anbu on 27/09/15.
 */
class BinarySplitTest extends Specification {

    def "Splitting file"() {
        given:
        ByteArrayInputStream bais=new ByteArrayInputStream([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                                                            123,124,125,126, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                                                            123,124,125,126, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                                                            123,124,125,126, 1,2,3,4,5,6,7,8,9,10
        ] as byte[])
        BinarySplit splitter=new BinarySplit(signature: [123,124,125,126] as byte[], inStream: bais)
        def bfw=new StringBinaryFileWriter()

        when:
        splitter.split(bfw)

        then:
        bfw.accumulatorList.size() == 4
        bfw.accumulatorList[0] == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] as byte[]
        bfw.accumulatorList[1] == [123,124,125,126, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] as byte[]
        bfw.accumulatorList[2] == [123,124,125,126, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] as byte[]
        bfw.accumulatorList[3] == [123,124,125,126, 1,2,3,4,5,6,7,8,9,10] as byte[]
    }

    def "Splitting file empty"() {
        given:
        ByteArrayInputStream bais=new ByteArrayInputStream([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] as byte[])
        BinarySplit splitter=new BinarySplit(signature: [123,124,125,126] as byte[], inStream: bais)
        def bfw=new StringBinaryFileWriter()

        when:
        splitter.split(bfw)

        then:
        bfw.accumulatorList.size() == 1
        bfw.accumulatorList[0] == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] as byte[]
    }

    def "Splitting file - only signature"() {
        given:
        ByteArrayInputStream bais=new ByteArrayInputStream([123,124,125,126] as byte[])
        BinarySplit splitter=new BinarySplit(signature: [123,124,125,126] as byte[], inStream: bais)
        def bfw=new StringBinaryFileWriter()

        when:
        splitter.split(bfw)

        then:
        bfw.accumulatorList.size() == 1
        bfw.accumulatorList[0] == [123,124,125,126] as byte[]
    }

    def "Splitting false positive"() {
        given:
        ByteArrayInputStream bais=new ByteArrayInputStream([1,2,3,4,5,123,124,125,34,5] as byte[])
        BinarySplit splitter=new BinarySplit(signature: [123,124,125,126] as byte[], inStream: bais)
        def bfw=new StringBinaryFileWriter()

        when:
        splitter.split(bfw)

        then:
        bfw.accumulatorList.size() == 1
        bfw.accumulatorList[0] == [1,2,3,4,5,123,124,125,34,5] as byte[]
    }
}
