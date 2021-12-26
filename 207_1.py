struct NodeTag{
    int flag;
    BiNode *BNode
}
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#define Maxsize 10000
using namespace std;

struct BiNode
{
    string data;
    BiNode *lchild, *rchild;
};
typedef BiNode *BiTree;

int InitBiTree(BiTree &T)
{
    T = NULL;
    return 0;
}

// 非递归后序遍历，返回遍历结果字符串
string
SucTraverse_nonRec(BiTree
T)
{
BiTree
stack[Maxsize];
int
top = -1;
BiTree
p = T;
bool
flag;
while (p != NULL | | top != -1){
while (p){
stack[++ top] = p;
flag=0;
p = p->lchild;
}
if (top != -1){
p=stack[top];
if (flag == 0)
{p = p->rchild;
flag=1;
}
else {
cout << p->data;
p=NULL;
top --;
}

}
}
// please
write
your
code
he
return " ";
}

// 用带虚结点的前序遍历串str（每个字符对应一个结点）构造二叉树T，并返回剩余字符串
char *CreateBiTree(BiTree &T, char *str)
{
    // 约定#表示空结点
    if (*str == '#')
    {
        T = NULL;
        return str + 1;
    }

    // 创建结点
    T = new BiNode;
    T->data = *str;

    // 继续输入并构造左子树和右子树
    char * strAfterLeft = CreateBiTree(T->lchild, str + 1);
    char * strAfterRight = CreateBiTree(T->rchild, strAfterLeft);

    // 返回剩余的字符串
    return strAfterRight;
}

int SucTraverse(BiTree T){
    if (T == NULL) return 0;
    SucTraverse(T->lchild);
    SucTraverse(T->rchild);
    cout << T->data;
    return 0;
}

int DestroyBiTree(BiTree &T){
    if (T == NULL) return 0;
    DestroyBiTree(T->lchild);
    DestroyBiTree(T->rchild);
    delete T;
    T = NULL;
    return 0;
}

// please comment the following code when you sumbit to OJ
int main(){
    // char *str = "abd###ceg##h##f#i##";
    char str[2000];
    while(cin >> str)
    {
        BiTree tree;
        InitBiTree(tree);
        // 根据带空节点的前序遍历字符串构造二叉树
        CreateBiTree(tree, str);
        // 后序遍历递归算法
        SucTraverse(tree);
        cout << endl;
        // 后序遍历非递归算法
        string result = SucTraverse_nonRec(tree);
        cout << result << endl;
        DestroyBiTree(tree);
    }
    return 0;
}