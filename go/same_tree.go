/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(p *TreeNode, q *TreeNode) bool {
    // If both nodes are nil, they are the same
    if p == nil && q == nil {
        return true
    }
    
    // If either node is nil, they are not the same
    if p == nil || q == nil {
        return false
    }
    
    // If the values of the nodes are different, they are not the same
    if p.Val != q.Val {
        return false
    }
    
    // Recursively check if the left and right subtrees are the same
    return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}