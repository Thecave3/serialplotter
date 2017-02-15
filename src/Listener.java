import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class Listener implements ActionListener {
	
	private final static String START = "start";
	private final static String STOP = "stop";
	private final static String CLEAN = "clean";
	
	GUI frame;
	
	Lettore read;
	Thread t;
	
	public Listener(GUI frame){
		this.frame = frame;
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getActionCommand().equals(START)){
			this.frame.serial.setEditable(false);
			this.frame.start.setEnabled(false);
			this.frame.clean.setEnabled(true);
			read= new Lettore();
			t = new Thread(read);
			t.start();
			
			this.frame.stop.setEnabled(true);
		}
		
		if(e.getActionCommand().equals(STOP)){
			this.frame.clean.setEnabled(false);
			this.frame.stop.setEnabled(false);
			try {
				t.join();
			} catch (InterruptedException e1) {
				System.out.println(e1.getMessage());
			}
			this.frame.start.setEnabled(true);
			this.frame.serial.setEditable(true);
			
			
		}
		
		if(e.getActionCommand().equals(CLEAN)){
			//CLEANING
		}

	}

}
