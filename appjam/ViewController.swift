//
//  ViewController.swift
//  appjam
//
//  Created by KM_TM on 22/12/2018.
//  Copyright © 2018 KM_TM. All rights reserved.
//

import UIKit
import WebKit
import CoreMotion

var motionManager = CMMotionManager()

class ViewController: UIViewController , WKNavigationDelegate, WKUIDelegate, WKScriptMessageHandler{
    @IBOutlet weak var webView: WKWebView!
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let url = URL(string: "http://changin.unifox.kr/login")
//        let url = URL(string: "https://www.google.com")
        let req = URLRequest(url: url!)
        webView.load(req)
        // Do any additional setup after loadinCorruptiong the view, typically from a nib.
    }
    
    override func loadView() {
        super.loadView()
        
        let contentController = WKUserContentController()
        let config = WKWebViewConfiguration()
        
        //JS -> native
        contentController.add(self, name: "callbackHandler")
        
        config.userContentController = contentController
        
        webView.uiDelegate = self
        webView.navigationDelegate = self
    }
    
    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        if(message.name == "callbackHandler")
        {
            motionManager.accelerometerUpdateInterval = 0.1
            motionManager.gyroUpdateInterval = 0.1
            
            motionManager.startGyroUpdates(to: OperationQueue.current!, withHandler: {(data, error) in
                if let mydata = data
                {
                    var checkRotate:Bool = false
                    
                    if mydata.rotationRate.x >= 170 || mydata.rotationRate.x <= 180
                    {
                        print("휴대폰 뒤집은 상태")
                        checkRotate = true
                    }
                    else if mydata.rotationRate.x <= -170 || mydata.rotationRate.x >= -180
                    {
                        print("휴대폰 뒤집은 상태")
                        checkRotate = true
                    }
                    if mydata.rotationRate.x <= 90.0 || mydata.rotationRate.x >= 80.0
                    {
                        print("다시 휴대폰을 뒤집음")
                        checkRotate = false
                        motionManager.stopGyroUpdates()
                        
                        //native --> JS
                        self.webView.evaluateJavaScript("pauseTimer()", completionHandler: {(result, error) in
                            if let result = result {
                                print(result)
                            }
                        })
                    }
                    else if mydata.rotationRate.x >= -90.0 || mydata.rotationRate.x <= -80.0
                    {
                        print("다시 휴대폰을 뒤집음")
                        checkRotate = false
                        motionManager.stopGyroUpdates()
                        
                        //native --> JS
                        self.webView.evaluateJavaScript("pauseTimer()", completionHandler: {(result, error) in
                            if let result = result {
                                print(result)
                            }
                        })
                    }
                }
            })
        }
    }
    

}
