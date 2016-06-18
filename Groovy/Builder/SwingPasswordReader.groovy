import groovy.swing.SwingBuilder

swing = new SwingBuilder()

frame = swing.frame(title: 'Password') {
    passwordField(columns: 10, actionPerformed: { event -> 
        println event.source.text
        System.exit(0)
    })
}

frame.pack()
frame.visible = true
