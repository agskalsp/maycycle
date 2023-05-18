package com.lynda.util;

import java.util.Date;
import org.apache.commons.lang.time.DateFormatUtils;

public class DateUtil {

        public static String getToday() {
                String today = DateFormatUtils.format(new Date(), "dd-MMM-yyyy");
				
                return today;
        }
}