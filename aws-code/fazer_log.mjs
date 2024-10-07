import { PutCommand } from "@aws-sdk/lib-dynamodb";
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient } from "@aws-sdk/lib-dynamodb";

export default async function fazer_log(response, id, payload) {
    const TableName = 'MusicRecommendationsLogs'
    
    const client = new DynamoDBClient({});
    const docClient = DynamoDBDocumentClient.from(client);
    
  try {
    console.log("Logging response:", response);
    
    const parsedBody = JSON.parse(response.body);
    const message = parsedBody.message; 

    const command = new PutCommand({
        TableName: TableName,
      Item: {
        requestId: id,       
        userId: '1',
        userRequest: payload.prompt,         
        gptResponse: message, 
        timestamp: new Date().toISOString()
      },
    });
    
    await docClient.send(command);
    return { statusCode: 200, body: 'Log registrado com sucesso.' };

  } catch (error) {
    console.error("Error while logging response:", error);
    return null;
  }
}
