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
     * @param {number} val
     * @return {TreeNode}
     */
    insertIntoBST(root: TreeNode | null, val: number): TreeNode {
        if(!root)
            return new TreeNode(val=val);
        else if (val < root.val){ // curr val is smaller than root val
            root.left = this.insertIntoBST(root.left, val);
        }else{
            root.right = this.insertIntoBST(root.right, val);
        }
        return root;
    }
}
