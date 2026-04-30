import emailjs from '@emailjs/browser';

const SERVICE_ID  = import.meta.env.VITE_EMAILJS_SERVICE_ID  || "";
const TEMPLATE_ID = import.meta.env.VITE_EMAILJS_TEMPLATE_ID || "";
const PUBLIC_KEY  = import.meta.env.VITE_EMAILJS_PUBLIC_KEY  || "";

/**
 * Sahayak AI — EmailJS Utility
 * Used for sending patient reports and alerts.
 */
export async function sendEmail(params: Record<string, any>) {
  if (!SERVICE_ID || !TEMPLATE_ID || !PUBLIC_KEY) {
    console.warn("EmailJS: Missing configuration (Service/Template/Key).");
    return false;
  }
  
  try {
    const response = await emailjs.send(SERVICE_ID, TEMPLATE_ID, params, PUBLIC_KEY);
    console.info("EmailJS: Success", response.status, response.text);
    return response.status === 200;
  } catch (error) {
    console.error("EmailJS: Error", error);
    return false;
  }
}
