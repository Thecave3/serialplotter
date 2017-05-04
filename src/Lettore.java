
public class Lettore implements Runnable {
	
	private GUI frame;
	
	public Lettore(GUI frame){
		this.frame = frame;
	}
	

	@Override
	public void run() {
		this.frame.data.setText("BUBU");
	}

}
