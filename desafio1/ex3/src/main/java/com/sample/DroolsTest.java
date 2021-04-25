package com.sample;

import org.kie.api.KieServices;
import org.kie.api.runtime.KieContainer;
import org.kie.api.runtime.KieSession;

public class DroolsTest {

    public static final void main(String[] args) {
        try {
            // load up the knowledge base
	        KieServices ks = KieServices.Factory.get();
    	    KieContainer kContainer = ks.getKieClasspathContainer();
        	KieSession kSession = kContainer.newKieSession("ksession-rules");
        	
        	System.out.println("\n\n");
        	
        	Pessoa jose = new Pessoa("José");
        	Pessoa manuel = new Pessoa("Manuel");
        	Pessoa joaquim = new Pessoa("Joaquim");
        	
        	boolean estadoInicial = false;
        	Sala sala = new Sala(19, estadoInicial);
        	
        	System.out.println(String.format(" -> Sistema está %s", estadoInicial ? "ligado" : "desligado"));
    		System.out.println(String.format(" -> Temperatura ambiente: %d\n", sala.getTemperatura()));
        	
        	kSession.insert(manuel);
        	kSession.insert(jose);
        	kSession.insert(joaquim);
        	kSession.insert(sala);
        	kSession.fireAllRules();
        	
        } catch (Throwable t) {
            t.printStackTrace();
        }
    }
}






/*
Sala sala;
for (int temp = 8; temp <= 10; temp += 2) {
	for(boolean estadoInicial : new boolean[] {true, false}) {
		System.out.println(String.format("|| Temperatura da sala: %d ºC ||", temp));
		System.out.println(String.format("|| Sistema está %s ||\n", estadoInicial ? "ligado" : "desligado"));
		sala = new Sala(temp, estadoInicial);
		
		kSession.insert(jose);
    	kSession.insert(manuel);
    	kSession.insert(joaquim);
    	kSession.insert(sala);
    	kSession.fireAllRules();
	}            	
}
*/
