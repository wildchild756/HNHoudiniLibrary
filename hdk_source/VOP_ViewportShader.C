#include <stdlib.h>
#include <UT/UT_DSOVersion.h>
#include <UT/UT_StringStream.h>
#include <PRM/PRM_Include.h>
#include <OP/OP_OperatorTable.h>
#include <OP/OP_Input.h>
#include <VOP/VOP_Operator.h>
#include "VOP_ViewportShader.h"

using namespace Hnlib;

void newVopOperator(OP_OperatorTable *table)
{
    OP_Operator *op;
    op = new VOP_Operator(
        "viewportShader",
        "Viewport Shader",
        VOP_ViewportShader::myConstructor,
        VOP_ViewportShader::myTemplateList,
        VOP_ViewportShader::theChildTableName,
        0,
        1,
        "*",
        0,
        OP_FLAG_OUTPUT,
        0
    );

    table->addOperator(op);
}

static PRM_Name theTestColor("testColor", "Test Color");

PRM_Template VOP_ViewportShader::myTemplateList[] =
{
    PRM_Template(PRM_RGB, 3, &theTestColor, PRMoneDefaults),

    PRM_Template()
};

VOP_ViewportShader::VOP_ViewportShader(OP_Network *parent, const char *name, OP_Operator *entry) : VOP_Node(parent, name, entry)
{
}

VOP_ViewportShader::~VOP_ViewportShader()
{
}

OP_Node *VOP_ViewportShader::myConstructor(OP_Network *net, const char *name, OP_Operator *entry)
{
    return new VOP_ViewportShader(net, name, entry);
}

void VOP_ViewportShader::getInputNameSubclass(UT_String &name, int idx) const
{
    name.harden(inputLabel(idx));
}

int VOP_ViewportShader::getInputFromNameSubclass(const UT_String &name) const
{
    for (int i = 0; i < getNumVisibleInputs(); i++)
    {
	if (name == inputLabel(i))
	    return i;
    }
    return -1;
}

void VOP_ViewportShader::getInputTypeInfoSubclass(VOP_TypeInfo &type_info, int idx)
{
    type_info.setType(VOP_TYPE_COLOR);
}

void VOP_ViewportShader::getAllowedInputTypeInfosSubclass( unsigned idx, VOP_VopTypeInfoArray &type_infos)
{
    type_infos.append( VOP_TypeInfo( VOP_TYPE_COLOR));
}

void VOP_ViewportShader::getOutputNameSubclass(UT_String &name, int idx) const
{
    name.harden(outputLabel(idx));
}

void VOP_ViewportShader::getOutputTypeInfoSubclass(VOP_TypeInfo &type_info, int idx)
{
    type_info.setType(VOP_TYPE_COLOR);
}

OP_ERROR cookMe(OP_Context &context)
{
    
}
