import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

@SuppressWarnings("serial")
public class GUI extends JFrame {
	private final static String titolo = "Serial Plotter";
	
	private final static String START = "start";
	private final static String STOP = "stop";
	private final static String CLEAN = "clean";
	private final static String DEFAULT_DOOR = "/COM3/";
	private final static int NUM_COLS = 30;
	
	JButton start = new JButton("START");
	JButton stop = new JButton("STOP");
	JButton clean = new JButton("PULISCI");
	
	JLabel door = new JLabel("Porta Seriale:");
	JLabel data = new JLabel("I dati verranno visualizzati qui.");
	JLabel time = new JLabel("Tempo");
	
	JTextArea grafico = new JTextArea(NUM_COLS,NUM_COLS);
	
	JTextField serial = new JTextField(DEFAULT_DOOR,NUM_COLS);
	
	JPanel north = new JPanel();
	JPanel centre = new JPanel();
	JPanel insidecenter = new JPanel();
	JPanel southcenter = new JPanel();
	JPanel south = new JPanel();
	
	Listener listen;
	
	
	
	public GUI(){
		super(titolo);
		this.getContentPane().setLayout(new BorderLayout());
		this.listen = new Listener(this);
		
		this.add(north, BorderLayout.NORTH);
		this.add(centre, BorderLayout.CENTER);
		this.add(south,BorderLayout.SOUTH);
		
		this.north.setLayout(new FlowLayout());
		this.north.add(door);
		this.north.add(serial);
		
		this.centre.setLayout(new BorderLayout());
		this.centre.add(insidecenter, BorderLayout.CENTER);
		this.centre.add(southcenter, BorderLayout.SOUTH);
		
		this.insidecenter.setLayout(new BorderLayout());

		this.insidecenter.add(grafico,BorderLayout.CENTER);
		
		this.southcenter.setLayout(new FlowLayout());
		this.southcenter.add(data);
		this.southcenter.add(time);
		
		this.south.setLayout(new FlowLayout());
		this.south.add(start);
		this.south.add(stop);
		this.south.add(clean);
		
		this.start.setActionCommand(START);
		this.stop.setActionCommand(STOP);
		this.clean.setActionCommand(CLEAN);
		
		this.start.addActionListener(listen);
		this.stop.addActionListener(listen);
		this.clean.addActionListener(listen);
		
		
		this.stop.setEnabled(false);
		this.clean.setEnabled(false);
		
		this.pack();
		this.setMinimumSize(getMinimumSize());
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}

}
