package concurrencia;
import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class StubReducer extends Reducer<Text, IntWritable, Text, DoubleWritable> {
	
	private DoubleWritable value = new DoubleWritable(0);

  @Override
  public void reduce(Text key, Iterable<IntWritable> values, Context context)
      throws IOException, InterruptedException {

    /*
     * TODO implement
     */
	  double sum = 0;
	  for (IntWritable v: values) {
		  sum += v.get();
	  }
	  
	  value.set(sum);
	  
	  context.write(key, value);

  }
}