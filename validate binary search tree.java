class Solution {
    private Integer prev;

    public boolean isValidBST(TreeNode root) {
        prev = null;
        return dfs(root);
    }

    private boolean dfs(TreeNode root) {
        if (root == null) {
            return true;
        }
        if (!dfs(root.left)) {
            return false;
        }
        if (prev != null && prev >= root.val) {
            return false;
        }
        prev = root.val;
        if (!dfs(root.right)) {
            return false;
        }
        return true;
    }
}
