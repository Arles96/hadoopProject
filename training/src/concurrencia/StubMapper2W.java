package concurrencia;
import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.commons.lang.math.NumberUtils;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class StubMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
	
	private final IntWritable one = new IntWritable(1);
	private Text word = new Text();

  @Override
  public void map(LongWritable key, Text value, Context context)
      throws IOException, InterruptedException {
	  
	  /*//Lo primero que se hace es leer la primera linea del archivo
	  final String [] values = value.toString().split(",");
	  
	  // El primer tipo de crimen esta en la sexta posicion
	  final String primaryType = values[5].toString();
	  
	  // La id del crimen esta en la octava posicion
	  final String id = values[7].toString();
	  
	  if (NumberUtils.isNumber(id.toString())) {		  
		  context.write(new Text(primaryType), new IntWritable(NumberUtils.toInt(id)));
	  }*/
	  
	  String line = value.toString();
	  StringTokenizer tokenizer = new StringTokenizer(line);

	  String prevWord = tokenizer.nextToken();
	  while (tokenizer.hasMoreTokens()) {
		  String thisWord = tokenizer.nextToken();
		  word.set(thisWord.concat(" ").concat(prevWord));
		  context.write(word, one);

		  prevWord = thisWord;
	  }	  
	  
  }
}
