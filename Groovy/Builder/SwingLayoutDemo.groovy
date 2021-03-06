import groovy.swing.SwingBuilder
import java.awt.BorderLayout as BL

swing = new SwingBuilder()
frame = swing.frame(title: 'Layout Demo') {
    panel(layout: new BL()) {
        button(constraints: BL.NORTH, 'North')
        button(constraints: BL.SOUTH, 'South')
        button(constraints: BL.EAST, 'East')
        button(constraints: BL.WEST, 'West')
        button(constraints: BL.CENTER, 'Center')
    }
}

frame.pack()
frame.visible = true
