import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY // Pass the API key here
});

export default async (payload) => {
  try {
    // Use the createChatCompletion method in OpenAI v4.x.x
    const completion = await openai.chat.completions.create({
      model: 'gpt-4o-mini',
      messages: [{ role: 'user', content: payload.prompt }],
    });

    // Get the response message
    const message = completion.choices[0].message.content;

    // Return the message as a response
    return {
      statusCode: 200,
      body: JSON.stringify({ message }),
    };
  } catch (error) {
    console.error('Error communicating with OpenAI:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({
        error: 'Failed to generate response from OpenAI.',
      }),
    };
  }
};


// import OpenAIApi from 'openai';

// export default async (payload) => {
//   // Retrieve OpenAI API key from environment variables
//   const OPENAI_API_KEY = process.env.OPENAI_API_KEY;

//   if (!OPENAI_API_KEY) {
//     console.error('OpenAI API Key is missing.');
//     return {
//       statusCode: 500,
//       body: JSON.stringify({
//         error: 'OpenAI API Key not configured.',
//       }),
//     };
//   }

//   const openai = new OpenAIApi({
//     apiKey: OPENAI_API_KEY,
//   });

//   try {
//     // Make a request to OpenAI to generate a response
//     const completion = await openai.createChatCompletion({
//       model: 'gpt-4',
//       messages: [{ role: 'user', content: payload.prompt }],
//     });

//     // Get the response message
//     const message = completion.data.choices[0].message.content;

//     // Return the message as a response
//     return {
//       statusCode: 200,
//       body: JSON.stringify({ message }),
//     };
//   } catch (error) {
//     console.error('Error communicating with OpenAI:', error);
//     return {
//       statusCode: 500,
//       body: JSON.stringify({
//         error: 'Failed to generate response from OpenAI.',
//       }),
//     };
//   }
// };
