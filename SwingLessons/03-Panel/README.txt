Lessons learnt:

* how to use flow layout - see ToolBar
* how to create panels - they are usually used to contain other components - see TextPanel & ToolBar
* how to modularise the component handling by implementing ActionListener interface - see ToolBar
* how to further modularise the components by having the controller, MainFrame, deal with component's 
  actions rather than passing reference of each component around - see MainFrame
* how to size components using setPreferredSize(Dimension)- tell layout manager what size the component 
  should be. - see FormPanel
* how to add borders using BorderFactory - see FormPanel. How to create a compound border containing 
  two or more borders.
* how to use GridBagLayout - see FormPanel. Align components within the grid, specify insets (padding)
  to the components.
* how to create a custom event and use that to pass events from a sub component to main frame.
* how to use a JList and how to use DefaultListModel to populate the options in the list.

Sequence of actions to be performed to replication this project:

* Create a MainFrame class of size 600x400
* Create a panel called TextPanel and put it at the middle of MainFrame to occupy all the area available. 
  The text panel contains one TextArea component. Wrap the text area with scroll bars.
* Create a panel called ToolBar with FlowLayout, and let it contain two buttons 'Hello' & 'Bye'
* On clicking the 'Hello' and 'Bye' buttons, the text area should have 'Hello' or 'Bye' appended to it
  automatically. 
* Create a FormPanel that accepts two text fields, name & occupation. In addition, create a 'Add' button 
  that will add the contents of the form fields to the text area.
* Create a new FormEvent class that extends java.util.EventObject and use that to handle the 'add'
  button's click event
* Add a new form list field for age category - 'Under 18', 'Over 18 but Under 65' and 'Over 65'.
* Add a new combo box with employment status 'employed', 'self-employed' or 'unemployed'.