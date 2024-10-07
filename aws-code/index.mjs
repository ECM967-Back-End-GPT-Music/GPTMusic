import enviar_gpt from './enviar_gpt.mjs'
import fazer_log from './fazer_log.mjs'

const funcoes = {
  "POST": async ({payload, id}) => {
    console.log("Executing POST function with payload:", payload);
    const response = await enviar_gpt(payload);
    
    await fazer_log(response, id, payload)
    
    return response;
  }
};

export const handler = async (event, context) => {
  
  const { method, payload } = event
  const id = context.awsRequestId
  try{
    return funcoes[method]({payload, id})
  }
  catch(e){
    console.log(event)
    return event
  }
}