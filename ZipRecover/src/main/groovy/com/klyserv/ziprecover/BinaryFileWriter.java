package com.klyserv.ziprecover;

import java.io.OutputStream;

/**
 * Created by anbu on 27/09/15.
 */
public interface BinaryFileWriter {
    OutputStream startWriting();

    void endWriting();
}
