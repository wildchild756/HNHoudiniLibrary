#ifndef __VOP_ViewportShader_h__
#define __VOP_ViewportShader_h__

#include <OP/OP_Error.h>
#include <VOP/VOP_Node.h>

namespace Hnlib
{
    class VOP_ViewportShader : public VOP_Node
    {
        public:
        static OP_Node *myConstructor(OP_Network *net, const char *name, OP_Operator *entry);

        static PRM_Template myTemplateList[];

        protected:
        VOP_ViewportShader(OP_Network *net, const char *name, OP_Operator *entry);
        ~VOP_ViewportShader() override;

        void getInputNameSubclass(UT_String &name, int idx) const override;
        int getInputFromNameSubclass(const UT_String &name) const override;
        void getInputTypeInfoSubclass(VOP_TypeInfo &type_info, int idx) override;
        void getAllowedInputTypeInfosSubclass(unsigned idx, VOP_VopTypeInfoArray &type_infos) override;
        void getOutputNameSubclass(UT_String &out, int idx) const override;
        void getOutputTypeInfoSubclass(VOP_TypeInfo &type_info, int idx) override;

        OP_ERROR cookMe(OP_Context &context) override;
    };
}

#endif
