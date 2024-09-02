// chatbot_integration.swift
import Foundation

func sendMessageToChatbot(userMessage: String) {
    let url = URL(string: "http://your-server-ip:5000/chatbot")!
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    let json: [String: Any] = ["text": userMessage]
    let jsonData = try? JSONSerialization.data(withJSONObject: json)

    request.httpBody = jsonData
    request.addValue("application/json", forHTTPHeaderField: "Content-Type")

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        guard let data = data, error == nil else {
            print("Error: \(error?.localizedDescription ?? "No data")")
            return
        }
        if let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 {
            if let responseString = String(data: data, encoding: .utf8) {
                print("Response from chatbot: \(responseString)")
                // Update the UI with the chatbot's response
            }
        }
    }
    task.resume()
}
