void FindMaxNum(int[] listOfNums)
{
    double maxSoFar = Double.NegativeInfinity;
    foreach (int num in listOfNums)
    {
        if (num > maxSoFar)
        {
            maxSoFar = num;
        }
    }
    Console.WriteLine("Max number: "+maxSoFar);
}