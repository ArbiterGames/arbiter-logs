# Arbiter Logging Server

Server for dumping json logs from Arbiter clients

## Usage

- Construct a chunk of json on the client. See the [client spec](https://docs.google.com/document/d/1U8wwrh9MwyoBcLME1bxCpQut4_xCRVp4Q6i335rU7Os/edit) for more info
- Create an HTTP POST with the json set as the `data` parameter

```objective-c

    NSDictionary *exampleJSONBlob = @{@"example_key", @"example value"};
    NSError *error = nil;
    NSString *url = @"http://logs.arbiter.me/report";
    NSData *paramsData = [NSJSONSerialization dataWithJSONObject:exampleJSONBlob
                                                         options:0
                                                           error:&error];
    NSString *paramsStr = [[NSString alloc] initWithData:paramsData encoding:NSUTF8StringEncoding];
    NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:url]
                                                           cachePolicy:NSURLRequestUseProtocolCachePolicy
                                                       timeoutInterval:60.0];
    [request setValue:@"application/json" forHTTPHeaderField:@"Content-Type"];
    [request setHTTPMethod:@"POST"];
    [request setHTTPBody:[paramsStr dataUsingEncoding:NSUTF8StringEncoding]];
    [NSURLConnection connectionWithRequest:request delegate:self];
```

- This will save the json blob as an `Entry` in the Arbiter Logs database.
- View all entries here: (http://logs.arbiter.me/admin/logs/entry/)[http://logs.arbiter.me/admin/logs/entry/]

## Roadmap

- pipe all entries along to mixpanel for presentation
