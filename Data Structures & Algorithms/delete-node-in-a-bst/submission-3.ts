/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    /**
     * @param {TreeNode} root
     * @param {number} key
     * @return {TreeNode}
     */
    getInOrderSuccessor(root:TreeNode):number{
        if(!root.left)
            return root.val
        return this.getInOrderSuccessor(root.left)
    }
    delNode(root:TreeNode | null, key:number): TreeNode | null {
            if(!root)
                return null
            if(root.val === key){
                //if no child
                if(!root.left && !root.right)
                    return null;
                else if (root.left && root.right){
                    //get in order sucessor
                    const v = this.getInOrderSuccessor(root.right)
                    root.val = v;
                    root.right = this.delNode(root.right, v);
                }else if(root.left){
                    root.val = root.left.val;
                    root.left = null;
                }else{
                    root.val = root.right.val;
                    root.right = null;
                }
            }
            else if(key < root.val)
                root.left = this.delNode(root.left, key)
            else
                 root.right = this.delNode(root.right,key)
            return root;
    }

    deleteNode(root: TreeNode | null, key: number): TreeNode {
        return this.delNode(root,key)
    }
}
