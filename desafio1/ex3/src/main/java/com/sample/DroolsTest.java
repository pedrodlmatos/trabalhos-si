package com.sample;

import org.kie.api.KieServices;
import org.kie.api.runtime.KieContainer;
import org.kie.api.runtime.KieSession;

//import com.sample.Pessoa;
//import com.sample.Temperatura;

/**
 * This is a sample class to launch a rule.
 */
public class DroolsTest {

    public static final void main(String[] args) {
        try {
            // load up the knowledge base
	        KieServices ks = KieServices.Factory.get();
    	    KieContainer kContainer = ks.getKieClasspathContainer();
        	KieSession kSession = kContainer.newKieSession("ksession-rules");
        	
        	//Temperatura temperatura = new Temperatura(30);
        	Temperatura temperatura = new Temperatura(8);
        	
        	Pessoa jose = new Pessoa("José");
        	Pessoa manuel = new Pessoa("Manuel");
        	Pessoa joaquim = new Pessoa("Joaquim");
        	
    
        	kSession.insert(temperatura);
        	kSession.insert(jose);
        	kSession.insert(manuel);
        	kSession.insert(joaquim);
        	kSession.fireAllRules();

            // go !
        	/*
            Message message = new Message();
            message.setMessage("Hello World");
            message.setStatus(Message.HELLO);
            kSession.insert(message);
            kSession.fireAllRules();
            */
        } catch (Throwable t) {
            t.printStackTrace();
        }
    }
    
    /*
    public static class Message {

        public static final int HELLO = 0;
        public static final int GOODBYE = 1;

        private String message;

        private int status;

        public String getMessage() {
            return this.message;
        }

        public void setMessage(String message) {
            this.message = message;
        }

        public int getStatus() {
            return this.status;
        }

        public void setStatus(int status) {
            this.status = status;
        }

    }
    */

}
