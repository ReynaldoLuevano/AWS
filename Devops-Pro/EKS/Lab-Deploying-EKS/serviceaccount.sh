eksctl create iamserviceaccount \
    --name iampolicy-sa \
    --namespace containers-lab \
    --cluster eks-lab-cluster \
    --role-name "eksRole4serviceaccount" \
    --attach-policy-arn arn:aws:iam::$ACCOUNT_NUMBER:policy/eks-lab-read-policy \
    --approve \
    --override-existing-serviceaccounts

kubectl set serviceaccount \
 deployment eks-lab-deploy \
 iampolicy-sa -n containers-lab


