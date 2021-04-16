package com.sample;

public class Sala {
	
	private int temperatura;		// temperatura da sala
	private boolean ligado;			// estado do sistema
	
	public Sala(int temperatura, boolean ligado) {
		this.temperatura = temperatura;
		this.ligado = ligado;
	}

	public int getTemperatura() {
		return temperatura;
	}

	public void setTemperatura(int temperatura) {
		this.temperatura = temperatura;
	}

	public boolean isLigado() {
		return ligado;
	}

	public void setLigado(boolean ligado) {
		this.ligado = ligado;
	}
	
	

}
