import os
import hou

def Convert(selection):
    nodePos = selection.position()
    nodeName = selection.name()
    obj = selection.parent()

    newNode = obj.createNode("subnet", nodeName + "_subnet")
    newNode.setPosition(nodePos)

    # copy items
    newNode.copyItems(selection.allItems())

    # wire input/output nodes
    nodeInputConnectors = selection.inputConnectors()
    for i in range(len(nodeInputConnectors)):
        connector = nodeInputConnectors[i]
        for j in range(len(connector)):
            newNode.setInput(i, connector[j].inputNode(), j)
    
    nodeOutputConnectors = selection.outputConnectors()
    for i in range(len(nodeOutputConnectors)):
        connector = nodeOutputConnectors[i]
        for j in range(len(connector)):
            outputNode = connector[j].outputNode()
            outputNode.setInput(connector[j].inputIndex(), newNode, i)
    
    # copy parameters
    group = selection.parmTemplateGroup()
    newNode.setParmTemplateGroup(group)

    selection.destroy()

