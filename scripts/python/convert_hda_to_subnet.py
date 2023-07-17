import os
import hou

def CopyParmsFromFolder(folderSet, parent):
    for parmTemplate in folderSet.parmTemplates():
        if isinstance(parmTemplate, hou.FolderSetParmTemplate):
            newFolder = hou.FolderParmTemplate(parmTemplate.name(), parmTemplate.label())
            newFolder.setFolderType(parmTemplate.folderType())
            CopyParmsFromFolder(parmTemplate, newFolder)
            parent.addParmTemplate(newFolder)
        else:
            newParm = parmTemplate.clone()
            parent.addParmTemplate(newParm)

def Convert(selection):
    nodePos = selection.position()
    nodeName = selection.name()
    obj = selection.parent()

    newNode = obj.createNode("subnet", nodeName + "_subnet")
    newNode.setPosition(nodePos)

    nodeInputConnectors = selection.inputConnectors()
    for i in range(len(nodeInputConnectors)):
        connector = nodeInputConnectors[i]
        for j in range(len(connector)):
            newNode.setInput(i, connector[j].inputNode(), j)
    
    nodeOutputConnectors = selection.outputConnectors()
    # print(nodeOutputConnectors)
    for i in range(len(nodeOutputConnectors)):
        if i > 0:
            newNode.createNode("output")
        connector = nodeOutputConnectors[i]
        for j in range(len(connector)):
            outputNode = connector[j].outputNode()
            # outputNode.setInput(connector[j].outputIndex(), newNode, i)
    
    group = newNode.parmTemplateGroup()
    baseFolder = hou.FolderParmTemplate("parmsFromHDA", "Parms From HDA")
    for parm in selection.parms():
        if isinstance(parm.parmTemplate(), hou.FolderSetParmTemplate):
            CopyParmsFromFolder(parm.parmTemplate(), baseFolder)
    group.append(baseFolder)
    newNode.setParmTemplateGroup(group)

    #     tmp = parm.tuple().parmTemplate()
    #     print(tmp)
    #     if parm.componentIndex() == 0:
    #         newParm = tmp.clone()
    #         newNode.addSpareParmTuple(newParm)
    #         group.append(newParm)
    # newNode.setParmTemplateGroup(group)

    # for parm in selection.parms():
    #     newParm = newNode.parm('parm')
    #     parm.copyToParmClipboard()
    #     clip = hou.parmClipboardContents()[0]
    #     path = clip['path']
    #     newParm.set(path)

